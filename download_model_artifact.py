import wandb
import argparse

def get_args_parser():
    parser = argparse.ArgumentParser('Download model saved as W&B Artifact and upload as Kaggle Dataset', add_help=False)
    parser.add_argument('--artifact_name', type=str,
                        help='URI of the artifact in the format <wandb id>/<wandb project name>/<artifact name>:latest')
    parser.add_argument('--root_path', type=str,
                        help="Path where the model will be downloaded")
    parser.add_argument('--project_name', type=str, default=None,
                        help='Name of the W&B project')
    return parser

def main(args):
    run = wandb.init(project=args.project_name)
    artifact = run.use_artifact(f'{args.artifact_name}:latest')
    artifact_dir = artifact.download(root=args.root_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Model download and upload script', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
