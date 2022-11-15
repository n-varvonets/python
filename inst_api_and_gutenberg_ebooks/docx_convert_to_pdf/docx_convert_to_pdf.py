import requests
import shutil
import groupdocs_conversion_cloud  # pip install groupdocs-conversion-cloud
import os

# 1. data for down file from alfresco
file_id = "edf00c65-df0a-4f9b-91ae-af0f63c35c01"
token = "VElDS0VUXzU2YzU5OGFiNmYxY2Q3MGZiMjMwOWY4OWUzZmU3MzlmNWZjYzNhY2E="

# 2. Any python internal libraries don't work for conversion docx2pdf. So I use external API.
# https://dashboard.groupdocs.cloud/applications - to get credentials. 150 free tries for trial.
client_id = "4538e74d-7fe1-4fcd-97a4-340c5ac3951d"
client_secret = "d696ce155a3c36153cbe104e04db3e43"

# 3. data for uploading converted pfd file in alfresco
relativePath_validity = "Sites/prime-estate/documentLibrary/03-CASES/{{owner} {name of case} {Sale}}/06-Delivries/01-ENGAGEMENT/validate"

# 4. local. The folder 'tempt_dir' should be at the same structure lvl with current script
path_to_tempt_dir = "/Users/1000geeks/PycharmProjects/python/tempt_dir"


def check_existing_tempt_folder(path_to_tempt_dir: str):
    """
    Check existing folder of tempt files.
    When you run the script, a new temporary folder will be created
    where you place the downloaded and verified file.
    After sending the pdf file, the created folder will be deleted
    """

    isExist = os.path.exists(path_to_tempt_dir)
    if not isExist:
        os.makedirs(path_to_tempt_dir)


def rename_converted_pdf():
    """ Renaming the file after API conversion """
    old_name = f"{path_to_tempt_dir}/my_file.pdf;"
    new_name = f"{path_to_tempt_dir}/my_file.pdf"

    os.rename(old_name, new_name)


def delete_tempt_folder():
    """Delete tempt folder with already send pdf file"""
    folder_path = path_to_tempt_dir
    try:
        shutil.rmtree(folder_path)
    except:
        print("The system cannot find the file specified")


def download_docx_from_alfresco(file_id: str, token: str):
    """Downloading docx doc from alfresco for local converting"""

    url = f"https://alfresco.prime-estate.1000geeks.com/alfresco/api/-default-/public/alfresco/versions/1/nodes/{file_id}/content?attachment=true"
    headers = {
        "accept": "application/octet-stream",
        "Authorization": "Basic " + token
    }

    raw_answer = requests.get(url, headers=headers)

    check_existing_tempt_folder(path_to_tempt_dir)

    with open(f"{path_to_tempt_dir}/my_file.docx", "wb") as binary_file:
        binary_file.write(raw_answer.content)


def convert_docx2pdf_via_API(client_id: str, client_secret: str):
    """Convert downloaded docx to pdf via API"""

    convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(client_id, client_secret)

    # Create convert request
    request = groupdocs_conversion_cloud.ConvertDocumentDirectRequest("pdf", f"{path_to_tempt_dir}/my_file.docx")

    # Convert
    result = convert_api.convert_document_direct(request)
    shutil.move(result, path_to_tempt_dir)


def upload_pdf(token: str, relativePath_validity: str):
    """Upload already converted pdf file to alfresco by rel path"""

    root_url_for_upload = "https://alfresco.prime-estate.1000geeks.com/alfresco/api/-default-/public/alfresco/versions/1/nodes/-root-/children"
    pdf_name_of_file = "new_pdf_filename.pdf"
    cm_from = "2022-10-10T08:00:00.000+0000"
    cm_to = "2022-12-27T15:00:00.000+0000"
    cm_title = "file_title with auto-rename and aspects"

    headers = {
        "Authorization": "Basic " + token,
    }
    data = {
        'name': pdf_name_of_file,
        'relativePath': relativePath_validity,
        'nodeType': 'cm:content',
        'autoRename': True,
        'cm:title': cm_title,
        'cm:from': cm_from,
        'cm:to': cm_to,
    }
    files = {
        'filedata': open(f"{path_to_tempt_dir}/my_file.pdf", 'rb')
    }

    response = requests.post(root_url_for_upload, headers=headers, data=data, files=files)


def main():
    """
    The script will move file in alfresco for any type cases
    from draft stage to validate with converting docx to pdf.
    """
    download_docx_from_alfresco(file_id, token)
    convert_docx2pdf_via_API(client_id, client_secret)
    rename_converted_pdf()
    upload_pdf(token, relativePath_validity)
    delete_tempt_folder()


if __name__ == '__main__':
    main()
