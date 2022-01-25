import wandb
print("Using W&B version: ", wandb.__version__)

wandb.login(anonymously=True)

run = wandb.init(anonymous='allow')
artifact = run.use_artifact('ayut/sr_ffhq/3jygvqe3_model:v26', type='model')
artifact_dir = artifact.download()
print(artifact_dir)
