# ClientDataCrawlerGUI - Your Automated Customer Data Management Tool

**ClientDataCrawlerGUI** is a powerful and automated customer data management tool designed to help you organize, search, and access customer-specific files and tasks efficiently. With this tool, you can seamlessly manage your customer data and streamline your workflow. Here's a detailed overview of the ClientDataCrawlerGUI project:

## Customer-Centric File Management

- **Folder Structure**: Each customer has a dedicated folder, and within these folders, you can organize various subfolders to represent specific customer requirements or tasks.

- **File Types**: Store scripts, Excel files, documents, and other related files in the corresponding task folders. This ensures that all customer-related data is neatly organized for easy access.

- **Name Files**: Each task folder contains a name file that identifies the stakeholder who requested the task. This enables you to search and access tasks based on the stakeholder's name.

## Streamlined Stakeholder Search

- **Efficient Searching**: You can search for tasks associated with specific stakeholders, such as salespeople responsible for multiple customers. For example, if you search for "Tobias," you'll instantly find all tasks from every company related to Tobias, saving you valuable time and effort. When searching for a file or script and you're unsure of the exact name, simply use the freetext search feature. For example, type something like: `company_xy*revenue*sql`
 and it will search for all SQL files that contain 'revenue' and the company name.

## GUI

- **Graphical User Interface**: The ClientDataCrawlerGUI might not have a fancy, modern look, but it gets the job done with minimal effort. It prioritizes functionality over aesthetics, making customer data management straightforward and efficient. Plus, you can easily enhance the code to improve its appearance if you wish. In essence, it's a dependable tool that keeps your customer data organized and accessible.

## Automated Updates

- **Automated Execution**: The provided `automate.bat` file allows you to automate tasks daily or weekly, ensuring that your application remains up-to-date. This automation guarantees that you always have access to the latest customer data.

## How to Use ClientDataCrawlerGUI

1. **Organize Customer Data**: Create a dedicated folder structure for each customer, organizing files and tasks based on their specific needs.

2. **Name Files**: In each task folder, include a name file that specifies the stakeholder responsible for the task.

3. **Run Automation**: Execute the `automate.bat` file to keep your application current and up-to-date. Check the `automate.bat` file to understand which script is when executed. You need all the provided files in the same folder as well your company logo. Everything else will do the .bat file for you

4. **Search Stakeholders**: Use the GUI to search for tasks and data associated with specific stakeholders, making data retrieval effortless.

5. **Access Customer Data**: With just a few clicks, you can access all customer-specific files and tasks from the user-friendly GUI.

## IMPORTANT: Customizing ClientDataCrawlerGUI for Your Environment

To adapt the ClientDataCrawlerGUI to your specific environment, you need to make a few key changes in the provided files. Here's a quick guide to what you should modify:

### File: main.spec

- **pathex=** → Update this to reflect your directory path where the Python scripts and resources are located.

- **datas=** → Replace this with the path to your company logo or any additional resources you want to include in the application.

- **name=** → Change this to your desired name for the executable file. Pick a name that makes sense for your organization.

### File: automate.bat

In the `automate.bat` file, there are specific steps you might need to customize:

#### Step 1: Run the Python script

- Modify the Python script command (`python C:\Users\maissento\mto\to_json_adhoc.py`) to match the actual path of your `to_json_adhoc.py` script in your environment.

#### Step 1.5: Remove existing folders

- Change the cd accordingly.

#### Step 3: Rename and move the .exe file

- Customize the path where the renamed `.exe` file should be moved. The `D:\RS\00_Test\adhoc_suche_%timestamp%.exe` path is just an example. Replace it with your desired destination folder.

## Showcase for better understanding

#### GUI 
On the left you can search for a person like tobias and find everyting related OR on the right the freetext search for files
I tried to show a picture but after I had censored everything with a black pen in my snipping... it looked terrible and didn't help either 

#### JSON looks like this
So within one person you will find every company assigned to it (if in each task-folder a .name file is)

```json
{
  "sales-person tobias maissen": {
    "Company_1": {
      "Revenue_YTD_2023": {
        "XLSX File": "",
        "SQL File": "",
        "PowerPoint": "",
        "tobias_maissen.name": "this is the name file"
      },
      "ProductSummary": {
        "XLSX File": "",
        "2 SQL File": "",
        "tobias_maissen.name": "this is the name file"
      }
    },
    "Company_8": {
      "Salesperformance_2020_2023": {
        "XLSX File": "",
        "SQL File": "",
        "PowerPoint": "",
        "tobias_maissen.name": "this is the name file"
      },
      "Product_XY_Analysis": {
        "XLSX File": "",
        "2 SQL File": "",
        "tobias_maissen.name": "this is the name file"
      }
    }
  }
}
