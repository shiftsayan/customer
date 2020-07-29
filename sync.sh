#!/bin/zsh
private_path=~/src/customer-private/
packs_path="$(dirname "$0")/packs"
now=$(date +"%m-%d-%Y")

echo "Copying private packs to private repository..."
cp $packs_path/*-private.pack $private_path

echo "Pushing changes to private repository..."
cd $private_path
git add .
git commit -m "Sync private packs on $now" &> /dev/null
git push &> /dev/null

echo "Sync complete!"