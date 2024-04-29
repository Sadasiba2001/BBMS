from django.urls import path
from BBMS_APP import views


urlpatterns = [
    # ************************** Without register *************************************
    path('login/', views.mainLogin, name='login'),
    path('userRegister/', views.userRegister, name='userRegister'),
    # ************************** Without register *************************************

    # ************************* For Customers ************************************************************************
    path('main-home/', views.mainHome, name='Home'),
    path('about/', views.about, name='about'),
    path('customerBloodOrder/', views.customerBloodOrder, name='customerBloodOrder'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('pricing', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonials, name='testimonials'),
    path('profile/', views.profile, name='profile'),
    path('bloodBankDetails/', views.bloodBankDetails, name='bloodBankDetails'),
    path('doctor_-_detail/', views.doctorDetails, name='doctor_details'),
    path('donor_-_details/', views.donorDetails, name='donor_details'),
    path('razorpay/checkout/<order_id>/', views.razorpay_checkout, name='razorpay_checkout'),
    path('razorpay/success/', views.razorpay_success, name='razorpay_success'),
    path('razorpay/callback/', views.razorpay_callback, name='razorpay_callback'),
    # ************************* For Customers ************************************************************************

    # ************************* For Admin usages ************************************************************************
    path('admin_-_home/', views.adminHome, name='admin_home'),
    path('admin_-_donorDetails/', views.adminDonorDetails, name='admin_donorDetails'),
    path('admin_-_donorRegistrationForm/', views.donorRegister, name='admin_donorRegistrationForm'),
    path('admin_-_donor_details_details/', views.adminDonorDetailsDetails, name='adminDonorDetailsDetails'),
    path('admin_-_DonorDetailsModification/', views.adminDonorDetailsModification, name='adminDonorDetailsModification'),
    path('admin_-_DonorBloodDonationRegisterPage', views.adminDonorBloodDonationRegisterPage, name='adminDonorBloodDonationRegisterPage'),
    path('admin_-_userDetails/', views.adminUserDetails, name='admin_userDetails'),
    path('admin_-_UserDetailsDetails/', views.adminUserDetailsDetails, name='adminUserDetailsDetails'),
    path('admin_-_BloodOrderHistory/', views.adminBloodOrderHistory, name='adminBloodOrderHistory'),
    path('admin_-_bloodStockDetails/', views.bloodStockDetails, name='admin_bloodStockDetails'),
    path('admin_-_doctorDetails/', views.adminDoctorDetails, name='admin_doctorDetails'),
    path('admin_-_doctorRegisterPage/', views.doctorRegisterPage, name='doctorRegisterPage'),
    path('admin_-_doctorDetailsDetailsPage/', views.doctorDetailsDetailsPage, name='doctorDetailsDetailsPage'),
    path('admin_-_doctorDetailsModificationPage/', views.doctorDetailsModificationPage, name='doctorDetailsModificationPage'),
    path('admin_-_logout/', views.adminLogout, name='admin_logout'),
    # ************************* For Admin usages ************************************************************************
]

# Define a handler for 404 errors
handler_404 = 'BBMS_APP.views.custom_404'
