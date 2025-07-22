cat /etc/passwd | grep -v '^#' | awk 'NR % 2 == 0' | cut -d: -f1 | sed 's/.*/&_/' | rev | sed -n "${FT_LINE1},${FT_LINE2}p" | sort -r | paste -sd ', ' - | sed 's/$/./'
