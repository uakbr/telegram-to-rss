# Telegram Channel-to-RSS

![tgtorss](https://i.imgur.com/chb0P9O.png)

This project is a Python script which fetches messages from Telegram channels and posts them to an RSS feed. It utilizes Azure Cloud Infrastructure to function.

## Installation and Configuration

The following instructions will help you in deploying the tg-channel-to-rss on Azure infrastructure.

### Prerequisites

* Azure Cloud subscription.
* Azure Functions Core Tools.
* Azure CLI.
* Docker and Docker Hub account.

### Installation Steps

#### 1. Clone the repository

Clone the [repository](https://github.com/hleb-kastseika/tg-channel-to-rss) from GitHub to a local directory.

#### 2. Create Azure resources

To create Azure resources follow these steps:

* Create a new [Azure Function App](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser#azure-cli) using the Azure CLI or Azure portal. 
* Create an [Azure Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal) to store the function's logs and scripts.
* Create an [Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli) (ACR) to host the Docker container image for the Python-based function app.

#### 3. Configure Azure Function

Then follow these instructions:

1. Create a new Python-based function in the Azure Function and name it "tg-channel-to-rss".
2. Upload the cloned Python file and all dependencies to the function's root directory.
3. Install the required libraries for your function by running following command:

        pip install -r requirements.txt

4. In the function's settings, specify a cron schedule for the function to run periodically.
5. Configure the webhook in Telegram for the channel you want to fetch data. To do this, follow [these instructions](https://core.telegram.org/bots/api#setwebhook).
6. Update the `config.json` file with the relevant information including your Telegram bot token, Telegram channel id, and RSS feed url.
7. In the function's `appsettings.json` file, add the following configuration settings:

        "AzureWebJobsStorage": "{azure-storage-connection-string}",
        "Logging.StorageConnectionString": "{azure-storage-connection-string}"

You can generate a storage connection string from the Azure portal and then insert it into the `appsettings.json` file.

#### 4. Set up containerization

Follow these steps to containerize the function app and deploy to ACR:

1. Sign in to your Docker account on your local machine by running `docker login`.
2. Build your Docker image by running following command:

        docker build -t {your-dockerhub-username}/tg-channel-to-rss .

This will create an image of the function app with all its dependencies.

3. Deploy the Docker image to ACR using the following command:

        docker push {your-dockerhub-username}/tg-channel-to-rss

4. In your Function App, go to "Platform features" and then "Container settings".
5. Set the "Image source type" to "Azure Container Registry".
6. Set the "Registry" to your ACR instance's URL and set the "Image and tag" to the Docker image you just pushed.

Now your function app is containerized and hosted on ACR!

## Credits

This project is built using [hleb-kastseika/tg-channel-to-rss](https://github.com/hleb-kastseika/tg-channel-to-rss) as a reference for the Python script.

-------

## Step-by-step guide to deploying `tg-channel-to-rss` on Azure Functions:

## Prerequisites

- A Microsoft Azure account
- Python 3.x installed on your local machine
- Azure CLI v2.0.80 or later installed on your local machine
- Git installed on your local machine
- An IDE or text editor (e.g. Visual Studio Code, PyCharm Community, etc.) for editing Python files

## Deployment Steps

### Step 1: Clone repository

Clone the `tg-channel-to-rss` repository onto your local machine using `git clone https://github.com/username/tg-channel-to-rss.git`. Replace "username" with your GitHub username.

### Step 2: Create a virtual environment

Create a virtual environment for the project using `python3 -m venv env`.

Activate the virtual environment by running `. env/bin/activate`.

### Step 3: Install dependencies

Install the required Python dependencies using `pip install -r requirements.txt`.

### Step 4: Test the application

Before deploying the application, verify everything is working locally.

To test the application locally, run `python src/tg-channel-to-rss.py`. This command should generate an `rss.xml` file in the root directory of the project containing messages from the Telegram channel.

### Step 5: Create Azure Function app

Create a new Function App on Azure.

To do this:
1. Open the Azure Portal.
2. Click "Create a resource" in the top-left corner.
3. search for "Function App," select it and click "Create."
4. Fill in the required fields. Note that the selected "Runtime Stack" should be "Python."
5. Click "Create" at the bottom of the page.

### Step 6: Deploy the application

Deploy the `tg-channel-to-rss` application to Azure Functions.

To do this:
1. Open up a command prompt or terminal and navigate to the repository root.
2. Run `az login` and follow the prompts to authenticate.
3. Run `func azure functionapp publish <function_app_name> --build-native-deps`. This command will prompt you to create a new Storage Account.
4. This command deploys the code to the Azure Functions app and creates the Python environment.

### Step 7: Setup environment variables

Configure environment variables on Azure for the Telegram bot token, Telegram channel ID, and RSS feed URL.

To do this:
1. In the Azure Portal, navigate to the Function App you created.
2. Click on "Configuration" in the Function App's sidebar.
3. On the Configuration page, select "Application settings".
4. Add the following three keys and values required for this application:
    - `TELEGRAM_BOT_TOKEN`: The API token of the Telegram bot.
    - `TELEGRAM_CHANNEL_ID`: ID of the Telegram channel that you want to fetch messages from.
    - `RSS_FEED_URL`: URL of the RSS feed you want to post to.

Save these environment variables.

### Step 8: Test the deployed application

To test the deployed application:

1. In the Azure Portal, navigate to the Function App you created.
2. In the left sidebar, select "Functions".
3. Click on the function you want to run.
4. In the function's toolbar, select "Run".
5. You should see messages on the console showing the progress and output of the script. If everything is working properly, you should see messages from the Telegram channel appear in your RSS feed.
