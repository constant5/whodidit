#! /bin/bash

for entry in `ls ./cleaned_subs/`; do
    new_entry=$(printf $entry | sed -E ':a; s/(^|[^0-9])([0-9]{1})([^0-9]|$)/\10\2\3/g; ta')
    `mv ./cleaned_subs/$entry ./cleaned_subs/$new_entry`
done