from prefect import flow
from prefect.deployments import Deployment
from utilities.run_flow import run_flow


def deploy():
    deployment = Deployment.build_from_flow(
        flow=run_flow, name="weather-metrics-flow-deployment-dev"
    )
    deployment.apply()


if __name__ == "__main__":
    deploy()
