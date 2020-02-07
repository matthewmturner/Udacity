import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format, from_unixtime, to_timestamp


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']



def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark

def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = os.path.join(input_data, 'song_data/A/A/A/*.json')
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_columns = ['song_id', 'title', 'artist_id', 'year', 'duration']
    songs_table = df.select(songs_columns).dropDuplicates()
    
    # write songs table to parquet files partitioned by year and artist
    songs_output = os.path.join(output_data, 'songs_table.parquet')
    songs_table.write.partitionBy('year','artist_id').parquet(songs_output, mode="overwrite")
    print('songs_table saved')

    # extract columns to create artists table
    artists_columns = ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
    artists_table = df.select(artists_columns).dropDuplicates()
    artists_col_renames = ['artist_id as artist_id','artist_name as name', 'artist_location as location', \
                           'artist_latitude as latitidue', 'artist_longitude as longitude']
    artists_table = artists_table.selectExpr(artists_col_renames)
    
    # write artists table to parquet files
    artists_output = os.path.join(output_data, 'artists_table.parquet')
    artists_table.write.parquet(artists_output, mode="overwrite")
    print('artists_table saved')


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = os.path.join(input_data, 'log_data/2018/11/*.json')

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong')

    # extract columns for users table    
    users_table_columns = ['userId', 'firstName', 'lastName', 'gender', 'level']
    users_table = df.select(users_table_columns).dropDuplicates()
    users_col_renames = ['userId as user_id', 'firstName as first_name', 'lastName as last_name', 'gender as gender', 'level as level']
    users_table = users_table.selectExpr(users_col_renames)
    
    # write users table to parquet files
    users_output = os.path.join(output_data, 'users_table.parquet')
    users_table.write.parquet(users_output, mode='overwrite')
    print('users_table saved')

    # create timestamp column from original timestamp column
    df = df.withColumn('timestamp', to_timestamp(col('ts')/1000))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: str(datetime.fromtimestamp(int(x)/1000)))
    df =  df.withColumn('datetime', get_datetime('ts'))
    
    # extract columns to create time table
    time_table = df.select('timestamp',
                          hour('timestamp').alias('hour'),
                          dayofmonth('timestamp').alias('day'),
                          weekofyear('timestamp').alias('week'),
                          month('timestamp').alias('month'),
                          year('timestamp').alias('year'),
                          date_format('timestamp', 'u').alias('weekday'))
    
    # write time table to parquet files partitioned by year and month
    time_output = os.path.join(output_data, 'time_table.parquet')
    time_table.write.partitionBy('year','month').parquet(time_output, mode='overwrite')
    print('time_table saved')

    # read in song data to use for songplays table
    song_data = os.path.join(input_data, 'song_data/A/A/A/*.json')
    song_df = spark.read.json(song_data)

    # extract columns from joined song and log datasets to create songplays table
    cond = [df.artist == song_df.artist_name, df.song == song_df.title, df.page == 'NextSong']
    songplays_table = df.join(song_df, cond).select(df.timestamp,
                                                   df.userId.alias('user_id'),
                                                   df.level,
                                                   song_df.song_id,
                                                   song_df.artist_id,
                                                   df.sessionId.alias('session_id'),
                                                   song_df.artist_location.alias('location'),
                                                   df.userAgent.alias('user_agent'))

    # write songplays table to parquet files partitioned by year and month
    songplays_output = os.path.join(output_data, 'songplays_table.parquet')
    songplays_table.write.parquet(songplays_output, mode='overwrite')
    print('songplays_table saved')


def main():
    spark = create_spark_session()
    print(spark._jsc.hadoopConfiguration())
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://mt-dend/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
