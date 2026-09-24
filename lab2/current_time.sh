#!/bin/bash
END_HOUR=18
END_MIN=0

hour=$(date +%H)
min=$(date +%M)

now=$((10#$hour * 60 + 10#$min))
end=$((END_HOUR * 60 + END_MIN))

echo "Current time: $hour:$min"

if (( now >= end )); then
    echo "Work day is already over."
else
    left=$((end - now))
    echo "Work day ends after $((left / 60)) hours and $((left % 60)) minutes."
fi
