# Customer

Customer is an easy-to-use command-line based tool to manage custom words for online games like [skribbl](https://skribbl.io/). You can combine multiple packs to get a sizeable number of custom words to play with.

## Usage

Customer is best used as a script.

```
# Make customer executable
chmod +x ./customer.py

# See customer usage
./customer.py --help

# Run customer
# `mm` is a private pack
./customer.py covid smash mm --limit 100 --allow-dupes
```

If you want to add more packs with inside jokes with your friends and family, you can add a new file in the `packs` directory with a newline separated list of your custom words. Ideally, you should suffix the pack name with `-private.pack` to ensure it is correctly ignored by `git` if you decide to make a pull request.

If you are worried about storing your private packs on ephemeral local media, you can use `sync.sh` to copy all private packs to a private repository. You'll need to change the `private_path` variable before running as a regular shell script.

## Contribution

I’d love for you to help us expand this project!

If you want to help expand an existing pack, please submit a pull request adding your newline separated list of words at the end of the existing pack in the `packs` directory.

If you want to add a new custom word pack, please submit a pull request adding a new file in the `packs` direcotry with a newline separated list of words.

Please only add or modify one pack per pull request.