Each of the two directories in the "lo-fi-machine" directory–"processing" and "synthesis"–should have their own dependencies (in "packages"), a main Python file as an AWS Lambda entrypoint (a serverless computational engine that will run every time it is triggered), and a Dockerfile.

Each directory has its own Docker image that is also stored in a container from the Amazon Elastic Container Registry (ECR). This image makes up a Lambda function. To setup this and push changes, see https://docs.aws.amazon.com/lambda/latest/dg/images-create.html. Note that the Dockerfiles, ECR URIs, and Lambda functions probably already exist.

NOTE: For M1 Macs, because the system is on the arm64 architecture, must append this flag to the build command to build x86: --platform linux/amd64