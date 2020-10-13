## Library Management

App for managing Articles, Members, Memberships and Transactions for Libraries

#### License

MIT# library_management


A. Updating App

You can edit your app using any tools and push these changes to GitHub. To incorporate these changes to your ERPNext instance, simply go into the apps directory and issue a git pull command:

cd /home/{user}/frappe-bench/apps/library_management
git pull
Enter your username and token when prompted

Then migrate these into your ERPNext:

cd /home/{user}/frappe-bench
bench --site erpnext.domain.com migrate
Replace domain with your site erpnext.domain.com 2 with your site address.

B. Installing App from GitHub
To install app from your GitHub link for example on a new ERPNext instances:

cd /home/{user}/frappe-bench
bench get-app https://github.com/ahmedozmaan/library_management.git
bench install-app library_management
bench --site library migrate
C. Uninstalling/Removing App from ERPNext
You can remove the app from ERPNext by

bench --site library uninstall-app library_management
bench remove-app library_management
Hope you find this useful.

Thanks.
