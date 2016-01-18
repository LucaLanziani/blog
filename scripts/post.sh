#!/usr/bin/sh

# cd into script directory
SCRIPT_DIR="${BASH_SOURCE%/*}"
cd "${BASH_SOURCE%/*}" || exit

POST_FOLDER="content/posts"
FOLDER="$POST_FOLDER/$(date  +%G/%m)"

if [ ! -d "../$POST_FOLDER" ];
then
  echo ""
  echo "Cannot find the $FOLDER folder"
  echo "did you move the folder or the script"
  echo "the path is relative to the script position (./$SCRIPT_DIR)"
  echo ""
  exit 1
fi
mkdir -p "../$FOLDER"

SECONDSFROMEPOC=$(date +%s)
TITLE=$@
if [ "$TITLE" == "" ];
then
  TITLE=$SECONDSFROMEPOC
fi

FILENAME=$(echo "$TITLE" | iconv -t ascii//TRANSLIT | sed -r s/[^a-zA-Z0-9]+/-/g | sed -r s/^-+\|-+$//g | tr A-Z a-z)
POST_FILE="$FOLDER/$FILENAME.md"

cat > "../$POST_FILE" << EOF
Title: $TITLE
Date: $(date +"%G-%m-%d %k:%M")
Category: General
Status: draft
Tags: general, template
Email: luca@lanziani.com


This is a template for a post

You can add links in this [format][1]:

Or code like this:

\`\`\`
sudo openconnect --juniper https://endpoint
\`\`\`

Simple enough eh? ;)

[1]: https://daringfireball.net/projects/markdown/syntax#link
EOF

echo "$POST_FILE created and ready to be edited" 
