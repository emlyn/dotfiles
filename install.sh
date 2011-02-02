#!/usr/bin/env bash
for i in bin _*; do
    src="${PWD}/$i"
    dst="${HOME}/"$(echo "${i}" | sed s/^_/./)
    if [ -e "${dst}" ] && [ ! -h "${dst}" ]; then
        echo "${dst} already exists, saving as ${dst}.bak"
        mv "${dst}" "${dst}.bak"
    fi
	ln -sf ${src} ${dst}
done
