## **Medical System Rest Api**
**This is my educational project, which is made using Django Rest Framework.**
It represents the fundamentals of medical system, which is widely used by doctors in both private and public medical clinics. 
The Rest Api was created with consultations of experienced doctor.

There is a wide range of features, here you can see some of them:

 - CRUD operations with different objects + list of them with special filters and authorizations :
	 - Clients, who belong to certain clinic
	 -  Doctors, who belong to certain clinic
	 - Appointments, which belong to certain clinic
	  - Session results, which belong to certain clinic
	  - Admins, who belong to certain clinic
	  -  Staff, who belong to certain clinic
	 - Departments, which belong to certain clinic
    
 - Other special features:
	 - Sign Up for doctors, staff and admins + Token based authentication
	 - Monthly statistics for certain doctor( amount of all clients, amount of boys in the age of 1-16, amount of girls, amount of boys in the age of 17-18, amount of children in the age of 0-1 and amount of disabled children)
	 - Weekly statistics for certain doctor(the same approach as in monthly statistics, but only for current week)

**I would also like to explain the connections between different models:**

 - So in system there are different clinics, which can't "see" each
   other and interact with any objects. 
   
  - Each clinic is divided into departments, which in real life are
   clinic departments in various districts or even cities. 
   
  - Doctors, clients(patients), administrators and staff are linked to
   specific clinics. 
   
   - Appointment is a meeting of client and doctor in specific department.
   It obviously has such parameters as start and end time.
   
  - Session results are bounded with appointments. In simple words -
   there was an appointment and then we have results of it. It has such
   important characteristics as diagnosis, patient's complaints,
   examination results and some financial info.
