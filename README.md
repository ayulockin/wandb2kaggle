# W&B 2 Kaggle

## Who is this for?

Competiting in a Kaggle competition (seriously) requires to train a LOT of models with different hyperparameters and different splits of the dataset. You can use [Weights and Biases](https://wandb.ai/site) to keep track of all your experiments but what about models trained and saved during every experiments. To version control the models and keep track of the dependencies [Weights and Biases Artifacts](https://docs.wandb.ai/guides/artifacts) can be used.

However, many of the Kaggle competitions are "[code based](https://www.kaggle.com/docs/competitions#competition-formats)" and requires the trained (fine-tuned) model(s) as Kaggle dataset. This can be a repetitive and prone to error.  

Thus this action is primarily made for:
- Kagglers
- User of [Weights and Biases Artifacts](https://docs.wandb.ai/guides/artifacts)

## What does it do?

This action automates the process of uploading the latest version of the selected model saved as Artifacts as Kaggle Dataset.

When you **merge a pull request**, the GitHub action will kick off the workflow, where:

- The model saved as W&B Artifact is downloaded,
- automatically upload the model as Kaggle Dataset.

## Prerequisite 

In order to use the action you will have to have a [W&B account](https://wandb.ai/signup) (free) and [Kaggle profile](https://kaggle.com). You will have to put the W&B Access Token and Kaggle Username and Key as GitHub Secrets. 

- You can get your W&B Access Token by visiting: wandb.ai/authorize. Save it as GitHub Secrets with the key name `WANDB_KEY`.
- You can get your Kaggle Username and Key by visiting the settings page of your Kaggle profile. Save the username as `KAGGLE_USERNAME` and key as `KAGGLE_KEY`.
- You can learn more about Kaggle Secrets [here](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

## How to use?

You can copy the `main.yml` workflow file from `.github/workflow/` and modify the input parameters accordingly. 

```
- name: W&B Artifact to Kaggle Dataset
  uses: ayulockin/wandb2kaggle@v1
```

## Inputs

#### `artifact_name`

You can find the `artifact_name` by visitng the API tab of a model artifact page as shown in the image below. Notice the `use_artifact` code snippet. Don't provide the `:v0` as the action automatically uses the `latest` version of the artifact. 

<img width="1279" alt="image" src="https://user-images.githubusercontent.com/31141479/151680004-3d811778-480d-4cf9-a126-644282526354.png">

#### `id`

Dataset identifier in format `{username}/{dataset}`. `username` is your Kaggle username.

#### `title`

Title of the Kaggle dataset.

#### `is_public`

If `true` the created Kaggle dataset is public. 

## Note

The provided `main.yml` file triggers the workflow when a commit is made to the `main` branch. It would be a good practice to use Pull Request. Here's a [list of events](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) that can trigger a workflow. 

## Acknowledgement

The action uses [Push kaggle dataset](https://github.com/marketplace/actions/push-kaggle-dataset) under the hood. Big shout out to [Jaime Valero](https://github.com/jaimevalero).

(* This is not an official Weights and Biases product.)
