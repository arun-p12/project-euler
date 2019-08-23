#!/bin/sh

i=51
while [ $i -le 100 ] ; do
  if [ $i -lt 10 ] ; then
     file="p000$i.py"
  elif [ $i -lt 100 ] ; then
     file="p00$i.py"
  elif [ $i -lt 1000 ] ; then
     file="p0$i.py"
  else
     file="p$i.py"
  fi
  
  if [ -f $file ] ; then
    echo "testing $file"
    echo "================"
    /usr/local/bin/python3 $file
    echo ""
  fi
  i=$(( i+1 ))
done
