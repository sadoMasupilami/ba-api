import argparse
import time
import subprocess
import uuid
import logging

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description='Tests speed of CI/CD container pipelines')
parser.add_argument('--git_path',
                    type=str,
                    help='path where git repository is located',
                    default='.')
parser.add_argument('--tag',
                    type=str,
                    help='tag that will be used to push',
                    default=str(uuid.uuid4()))
parser.add_argument('--image',
                    type=str,
                    help='address of the docker registry',
                    required=True)
args = parser.parse_args()

logging.info("running: git tag -f {}".format(args.tag))
process = subprocess.run(["git", "tag", "-f", args.tag],
                         shell=True,
                         capture_output=True,
                         text=True,
                         cwd=args.git_path,
                         check=True)
logging.debug(process.stdout)

logging.info("running git push -f origin {}".format(args.tag))
process = subprocess.run(["git", "push", "-f", "origin", args.tag],
                         shell=True,
                         capture_output=True,
                         text=True,
                         cwd=args.git_path,
                         check=True)
logging.debug(process.stdout)

timeout = time.time() + 60 * 10  # 10 minutes from now
start = time.time()
logging.info("Starting loop waiting for image to appear")
while True:
    if time.time() > timeout:
        logging.error("timeout reached")
        break
    process = subprocess.run(
        ["docker",
         "manifest",
         "inspect",
         "{}:{}".format(args.image, args.tag)],
        shell=True,
        capture_output=True,
        text=True)
    if process.returncode == 0:
        break
    logging.info("still no image found after {} seconds"
                 .format(time.time() - start))
logging.info("image found!")
logging.debug(process.stdout)

print("time: {} seconds".format(time.time() - start))
