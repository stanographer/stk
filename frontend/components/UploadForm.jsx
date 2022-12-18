import React, { useState } from 'react';
import {
  Button,
  Form,
  FormGroup,
  Input,
  Label,
} from 'reactstrap';

const UploadForm = props => {
  const [selectedFile, setSelectedFile] = useState({});
  const [isSelected, setIsSelected] = useState(false);
  const [fileUploadSuccessful, setFileUploadSuccessful] = useState(false);
  const [uploadResultText, setUploadResultText] = useState({});

  const uploadHandler = event => {
    const formData = new FormData();

    formData.append('file', selectedFile);

    event.preventDefault();

    fetch(process.env.NEXT_PUBLIC_UPLOAD_ENDPOINT, {
      method: 'POST',
      body: formData,
      contentType: 'application/json',
    })
      .then(res => res.json())
      .then(json => successHandler(json))
      .catch(error => console.error('error', error));
  };

  const changeHandler = event => {
    setSelectedFile(event.target.files[0]);
    setIsSelected(true);
  };

  const successHandler = responseText => {
    setFileUploadSuccessful(true);
    setUploadResultText(responseText);
  };

  const UploaderForm = () => (
    <>
      { isSelected ?
              (
                <div>
                  <p>filename: {selectedFile.name}</p>
                  <p>file type: {selectedFile.type}</p>
                  <p>size: {selectedFile.size}</p>
                  <p>last modified: {selectedFile.lastModifiedDate.toLocaleDateString()}</p>
                </div>
              ):
              (
                <Input type="file"
                  id="file"
                  name="file"
                  onChange={changeHandler}
                />
              )
            }
      <Button type="submit"
        color="success"
        onClick={event => uploadHandler(event)}
        disabled={!isSelected}
        >
          upload
      </Button>
    </>
  );

  const { action } = props;

  return (
    <Form encType='multipart/form-data'>
      <FormGroup>
        <Label for="exampleCustomFileBrowser">Dictionary Uploader</Label>
          { !fileUploadSuccessful ? <UploaderForm></UploaderForm> : <p>{uploadResultText.fileName}</p>}
      </FormGroup>
    </Form>
  )
};

export default UploadForm;
