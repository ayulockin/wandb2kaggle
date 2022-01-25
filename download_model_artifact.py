import wandb
print("Using W&B version: ", wandb.__version__)

run = wandb.init()
artifact = run.use_artifact('ayut/sr_ffhq/3jygvqe3_model:v26', type='model')
artifact_dir = artifact.download()
print(artifact_dir)
