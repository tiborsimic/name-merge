import torch
from sentence_transformers import SentenceTransformer

from sample import canonical_names, name_variants

# uncomment for alternative model
# model = SentenceTransformer("all-MiniLM-L6-v2")

model = SentenceTransformer("waynedsouza/only_names")

embeddings_canonical = model.encode(canonical_names)
embeddings_variants = model.encode(name_variants)

distances = model.similarity(embeddings_variants, embeddings_canonical)
max_similarity_score, max_similarity_index = torch.max(distances, dim=1)

for i, (score, index) in enumerate(zip(max_similarity_score, max_similarity_index)):
    print(f'{name_variants[i]},{canonical_names[index]},{score}')


if __name__ == "__main__":
    pass



