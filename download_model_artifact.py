import wandb
from argparse

def get_args_parser():
  parser = argparse.ArgumentParser('Download model saved as W&B Artifact and upload as Kaggle Dataset', add_help=False)
  parser.add_argument('--artifact_name', default=64, type=int,
                        help='Per GPU batch size')


run = wandb.init()
artifact = run.use_artifact('ayut/sr_ffhq/3jygvqe3_model:v26', type='model')
artifact_dir = artifact.download()
print(artifact_dir)
