hf download karpathy/nanochat-d32
mkdir -p ~/.cache/nanochat/tokenizer/
mkdir -p ~/.cache/nanochat/chatsft_checkpoints/d32
cp ~/.cache/huggingface/hub/models--karpathy--nanochat-d32/snapshots/016dba034c9c0ca9033ad1bc721bceff54680600/tokenizer.pkl ~/.cache/nanochat/tokenizer/
cp ~/.cache/huggingface/hub/models--karpathy--nanochat-d32/snapshots/016dba034c9c0ca9033ad1bc721bceff54680600/token_bytes.pt ~/.cache/nanochat/tokenizer/
cp -p ~/.cache/huggingface/hub/models--karpathy--nanochat-d32/snapshots/016dba034c9c0ca9033ad1bc721bceff54680600/token_bytes.pt ~/.cache/nanochat/tokenizer/
cp -p ~/.cache/huggingface/hub/models--karpathy--nanochat-d32/snapshots/016dba034c9c0ca9033ad1bc721bceff54680600/meta_000650.json ~/.cache/nanochat/chatsft_checkpoints/d32/
cp -p ~/.cache/huggingface/hub/models--karpathy--nanochat-d32/snapshots/016dba034c9c0ca9033ad1bc721bceff54680600/model_000650.pt ~/.cache/nanochat/chatsft_checkpoints/d32/