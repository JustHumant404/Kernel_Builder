#!/bin/bash
KSU_API_VERSION=$(curl -fsSL "https://raw.githubusercontent.com/SukiSU-Ultra/SukiSU-Ultra/$BRANCH_NAME/kernel/Makefile" | \
  grep -m1 "KSU_VERSION_API :=" | awk -F'= ' '{print $2}' | tr -d '[:space:]')

if [ -z "$KSU_API_VERSION" ]; then
  echo "Error:KSU_API_VERSION Not Found" >&2
  exit 1
fi
        
KSU_COMMIT_HASH=$(git ls-remote https://github.com/SukiSU-Ultra/SukiSU-Ultra.git refs/heads/susfs-main | awk '{print $1}' | cut -c1-8)

VERSION_DEFINITIONS=$(cat << 'EOF'
define get_ksu_version_full
v$1-${KSU_COMMIT_HASH}-@JustHumant404
endef

KSU_VERSION_API := ${KSU_API_VERSION}
KSU_VERSION_FULL := v${KSU_API_VERSION}-${KSU_COMMIT_HASH}-@JustHumant404
EOF
)
sed -i '/define get_ksu_version_full/,/endef/d' kernel/Makefile
sed -i '/KSU_VERSION_API :=/d' kernel/Makefile
sed -i '/KSU_VERSION_FULL :=/d' kernel/Makefile

awk -v def="$VERSION_DEFINITIONS" '
  /REPO_OWNER :=/ {print; print def; inserted=1; next}
  1
  END {if (!inserted) print def}
' kernel/Makefile > kernel/Makefile.tmp && mv kernel/Makefile.tmp kernel/Makefile

grep -A10 "REPO_OWNER" kernel/Makefile
grep "KSU_VERSION_FULL" kernel/Makefile
