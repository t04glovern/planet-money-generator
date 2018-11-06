# Planet Money - Podcast Generator

trained text-generating neural network that generates episodes of [Planet Money](https://www.npr.org/sections/money/)

```txt
KESTENBAUM: That is a count to Norway. Thee resorves of the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the wort of the oil curse. So the were on the oil curse. The problem is the resorves in the

SMITH: Yee. And it's to the recesterent of the recountry that was a lot of the oil curse. The problem is the oil curse. The problem with the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the oil curse. The problem is the oil cur
```

## CloudFormation

### SageMaker

Fill in the `sagemaker-notebook-params.json` file with your desired settings.

```json
[
    {
        "ParameterValue": "ml.t2.medium",
        "ParameterKey": "NotebookInstanceType"
    },
    {
        "ParameterValue": "sg-13371337",
        "ParameterKey": "SecurityGroupId"
    },
    {
        "ParameterValue": "subnet-1234123",
        "ParameterKey": "SubnetId"
    },
    {
        "ParameterValue": "planet-money-analysis",
        "ParameterKey": "NotebookInstanceName"
    },
    {
        "ParameterValue": "planey-money-generator",
        "ParameterKey": "SageMakerS3Bucket"
    }
]
```

```bash
aws cloudformation --region us-east-1 create-stack --stack-name planet-money-sagemaker \
    --template-body file://aws/sagemaker-notebook.json \
    --parameters file://aws/sagemaker-notebook-params.json \
    --capabilities "CAPABILITY_IAM" \
    --disable-rollback
```

### S3

Sync the transcripts to the chosen S3 bucket. If you would like to Scrape these yourself, you can use the `scrape.ipynb` notebook in the coming steps.

```bash
aws s3 sync transcripts/ s3://planey-money-generator/transcripts
```

## SageMaker Notebook Setup

Upload the contents of `notebooks/` to your SageMaker root directory.

![SageMaker example](img/sagemaker-example.png)

* `scrape.ipynb` - scrape the episode transcripts
* `basic-analysis.ipynb` - train your own text-generating neural network (uses [textgenrnn](https://github.com/minimaxir/textgenrnn))
* `basic-analysis-conversation.ipynb` - train and output a conversation log between reporters
