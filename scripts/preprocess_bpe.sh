#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Example call:
#   bash scripts/run_preprocessing.sh

set -e

raw_data=$1
# set languages
src_lang=$2
tgt_lang=$3

# set paths
scripts=`dirname "$(readlink -f "$0")"`
base=$scripts/..
bpe=$raw_data/../bpe
preprocessed=$raw_data/../preprocessed
prepared=$bpe/prepared

mkdir -p $bpe
mkdir -p $preprocessed
mkdir -p $prepared

# train bpe model
cat $preprocessed/train.$src_lang $preprocessed/train.$tgt_lang | gshuf > $bpe/train
spm_train --input=$bpe/train --model_prefix=$bpe/bpe --vocab_size=8000 --model_type=bpe

for lang in $src_lang $tgt_lang
    do
        echo "applying bpe model for $lang"

        # get vocab files from bpe model
        spm_encode --model=$bpe/bpe.model --generate_vocabulary < $preprocessed/train.$lang > $bpe/vocab.$lang

        for split in train tiny_train test valid
            do
                echo "preprocessing $split split for language $lang..."

                spm_encode --model=$bpe/bpe.model --vocabulary=$bpe/vocab.$lang < $preprocessed/$split.$lang > $bpe/$split.$lang

            done

    done

echo "preparing data for model training..."

python $base/preprocess.py \
    --source-lang $src_lang \
    --target-lang $tgt_lang \
    --dest-dir $prepared \
    --train-prefix $bpe/train \
    --valid-prefix $bpe/valid \
    --test-prefix $bpe/test \
    --tiny-train-prefix $bpe/tiny_train \
    --threshold-src 1 \
    --threshold-tgt 1 \
    --num-words-src 4000 \
    --num-words-tgt 4000

echo "done."
