#!/bin/sh
red=$(tput setaf 1)
normal=$(tput sgr0)

for i in *.py; do
  printf "$i "
  python3 -m doctest $i > $i.log
  if [[ $? -ne 0 ]]; then
    printf "${red}✗${normal}\n"
  else
    printf "✓\n"
  fi
done
