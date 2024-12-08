#                                                 IS601 Final Project: User Management System 
________________________________________
### Overview: 
The User Management System project [Project Link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management) has been a remarkable journey, providing a comprehensive, real-world coding experience that closely mirrors professional software development environments. As part of this project, I concentrated on enhancing user profile management by integrating the Profile Picture Upload feature using Minio. Additionally, I worked on improving system functionality by implementing robust validation mechanisms, handling edge cases, and ensuring seamless user interactions.
This project allowed me to deepen my understanding of backend development, database management, and the integration of third-party tools. I also honed my debugging and problem-solving skills while collaborating in a structured environment.
By adhering to best coding practices and leveraging tools like pytest for testing, I ensured the reliability and scalability of the features. This experience highlights my learning process, technical contributions, and personal growth throughout the project. It has significantly enhanced my ability to deliver efficient and user-centric solutions.
________________________________________
### Feature Implemented: Profile Picture Upload with Minio : [Feature Link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/pull/16)

This feature aims to improve user engagement by integrating profile picture upload functionality using Minio, a distributed object storage system. It provides users with the ability to personalize their accounts while ensuring secure and efficient management of profile pictures.This feature not only enhances user engagement by allowing profile personalization but also demonstrates the capability to integrate third-party systems like Minio effectively. By focusing on security, scalability, and user experience, it ensures a robust and user-centric implementation.
________________________________________
### Implementation Details:
1.	API Endpoint for Uploading Profile Pictures:
   
     o	Developed a POST /users/{id}/profile-picture API endpoint.
   
     o	Validate the uploaded files to ensure:
  	
     o	Supported formats: JPEG, PNG, GIF.
  	
  	 o	File size limits: e.g., up to 5MB.
  	
     o	Secure file names: Use unique identifiers (e.g., UUIDs) to prevent overwriting.
  	
2.	Secure Storage in Minio:
   
    o	Store profile pictures in a dedicated bucket.
  	
    o	Applied bucket policies to enforce strict access controls.
  	
3.	Enhancements to User Profile API:
   
    o	Extend the User schema to include a profile_picture_url field.
  	
    o	Update GET /users/{id} to return the profile picture URL alongside other user details.
  	
4.	Retrieve Profile Picture URL:
   
    o	Generate presigned URLs from Minio for secure and efficient retrieval.
  	
    o	Ensure the URLs are dynamically included in user profile responses.
________________________________________
### Key Considerations

1.	Validation:
   
     o	Enforce strict validation for file types and sizes to prevent misuse.
  
     o	Return clear error messages for invalid uploads.
  
2.	Security:
   
     o	Ensure all API communication occurs over HTTPS.
  
     o	Apply IAM policies to Minio buckets to restrict unauthorized access.
  
     o	Use presigned URLs with short expiration times for secure access.
  
3.	Scalability:
   
     o	Optimize bucket structure for large-scale storage.
  
     o	Implement caching for frequently accessed profile pictures.
  
4.	Error Handling:
   
      o	Return appropriate HTTP status codes:
  	
      o	400 Bad Request for invalid inputs.
    
      o	404 Not Found for missing user profiles or pictures.
   
      o	 500 Internal Server Error for unexpected issues.
________________________________________
### Benefits

  •	Personalizes user profiles, enhancing the overall user experience.

  •	Ensures secure and scalable management of profile pictures using Minio.

  •	Improves the API functionality by integrating additional features like retrieval and dynamic URL generation.

________________________________________
### Testing and Validation ###

•	Unit Tests:

  Validated file uploads for supported and unsupported file types.
  
  Verified correct integration with Minio for storage and retrieval.
  
•	Integration Tests:

   Tested the complete workflow from upload to display.
  
   Ensure API endpoints return correct data for valid and invalid inputs.

________________________________________
This submission meets the following goals:
1.	Implements a NEW feature into the existing codebase.
2.	Fixed 5+ QA Issues/Bugs across the codebase.
3.	Wrote 10+ NEW Tests for the new feature implemented.
4.	Includes a Reflection Document for the course.
5.	Includes Extensive Documentation of the feature, bugs and test cases implemented.
________________________________________
Issues Resolved:

Solved 5 major issues to improve the project:

1.	Fix the Docker File to allow build :  [Issue 1 link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/issues/5)

      •	Updated the Docker File to allow build.

      •	Fixed the workflow action yml file to pass the build if the vulnerabilities are found.

      •	Fixed the Application throwing error due to library version mismatch.
 
2.	User ID is passed as None in the user verification email:  [Issue 2 link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/issues/7)
   
    •	User ID is passed as None in the user verification email.
  	
    •	Email will be sent only once when the user is added and updated in the database.
  	
    •	Updated Code to fix user id showing as none in user verification email

3.	Enforce strong Password validation: [Issue 3 link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/issues/9)
   
    •	Fixed the code to enforce strong password validation. This fix will ensure that the password meets several security criteria, such as length, inclusion of upper and lower case letters, digits, special characters, and avoiding spaces.
  	
    •	Length Check: Ensures the password is at least 8 characters long.
  	
    •	Uppercase Check: Ensures at least one uppercase letter ([A-Z]).
  	
    •	Lowercase Check: Ensures at least one lowercase letter ([a-z]).
  	
    •	Digit Check: Ensures at least one numeric digit (\d).
  	
    •	Special Character Check: Ensures at least one character from a set of common special characters.
  	
    •	No Spaces: Ensures the password does not contain spaces (\s)

4.	Fix the valid profile picture uploads: [Issue 4 link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/issues/11)
   
    •	To ensure that the provided URL meets specific criteria, such as being well-formed and pointing to an image file.
  	
    •	Fixed the code to validate Proper URL format - Ends with valid image extensions (.jpg, .jpeg, .png, .gif)
  	
    •	To ensure secure and valid profile picture uploads, implemented robust URL validation by verifying that the input is a well-formed URL, ends with a standard image file extension such as .jpg, .png, or .gif, and optionally checking the URL's accessibility and content type to confirm it points to a valid image resource.

5.	Not able to update is professional user field [Issue 5 link](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/issues/13)
	
    •	The issue of not being able to update the is_professional field was resolved by identifying and addressing the missing field in the user schema.
    The is_professional field was added to both user_update and user_response schemas, ensuring proper data handling and seamless functionality for updates.
________________________________________
Testing and Quality Assurance :

•	Added 10+ test cases:  [Link for 10+ test cases](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/commit/4dc9cd63132d886d22672df0685b8845c6b55d54)

•	By implementing these test cases, we can ensure a robust and user-friendly profile picture upload feature, while maintaining the security and reliability of the MinIO storage backend. 

________________________________________
Deployment:

•	Successfully deployed the project to DockerHub :	[DockerHub Repository](https://hub.docker.com/repository/docker/mallikakasi/is601_finalproject_user_management/general)

•	Configured GitHub Actions for automated workflows :	[Successful Workflows](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management/actions)

•	GitHub Repository: [User Management Project](https://github.com/MallikaKasi/IS601-Fall2024-FinalTerm_Project_user_management)
________________________________________

