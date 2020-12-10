echo $(cat input.txt | sort -n | awk '{print $0-prev; prev=$0}' | grep ^1 | wc -l) "* (" $(cat input.txt | sort -n | awk '{print $0-prev; prev=$0}' | grep ^3 | wc -l) " +1)" | bc
