#!/bin/bash
START_DATE=$(date -d "20211201" +%Y-%m-%d)
BASE_CNT=90
for (( a = 1; a < $BASE_CNT; a++ ))
do
  curl --data "date=$START_DATE&content=Text of $START_DATE day&subject=Title of $START_DATE day" https://dry-lake-88654.herokuapp.com/news/
  START_DATE=$(date -d "$START_DATE+1 day" +%Y-%m-%d)
done

#curl --data "content=None day&subject=None day" https://dry-lake-88654.herokuapp.com/news/