	01.Download_Install_Prepare_OCP4_Binaries.yaml
        
	tasks: 
            1. Create temporary ocp binaries directory - /tmp/openshift-tools
            2. Create temporary mirror-registry directory /tmp/mirror-registry
            3. Download oc-mirror binaries
            4. Download OpenShift Client (oc & kubectl) binary
            5. Download OpenShift Installer binary
            6. Download Mirror Registry 
            7. Extract all ocp binaries tarballs 
            8. Ensure binaries are executable 
            9. Clean up temporary directories but not mirror-registry directory
           10. Verify installation - oc version 
           11. Display oc version


        02.Mirror_Registry_Configure.yaml

        tasks: 
            1. Ensure Red Hat Subscription Unregister system if already registered (optional cleanup)
            2. Clean subscription data
            3. Register system to Red Hat Subscription
            4. Attach available subscription (auto-attach)
            5. Enable required repositories
            6. Ensure required packages are installed
            7. Create registry directories - /opt/mirror-registry /opt/registry
            8. Download Mirror Registry tarball - mirror-registry.tar.gz
            9. Extract Mirror Registry package 
           10. Run Mirror Registry install script 
           11. Ensure Mirror Registry service is running
           12. Display Mirror Registry status
           13. Copy Red Hat and Quay secrets
           14. Log in to local mirror registry
           15. Log in to Red Hat and Quay.io registries
           16. Display registry login result

        03.Prepare_Install_Config_Manifests.yaml

        tasks: 
            1. Ensure required packages are installed (Apache + dependencies)
            2. Ensure Apache service is enabled and running
            3. Ensure OpenShift installation directory exists
            4. Create install-config.yaml for OpenShift 4
            5. Verify install-config.yaml exists
            6. Fail if install-config.yaml is missing
            7. Generate OpenShift manifests
            8. Generate ignition configs
            9. Ensure web server directory exists
           10. Copy ignition files to web server directory
           11. Adjust permissions for ignition files
           12. Set SELinux context for web directory
           13. Ensure firewall allows HTTP (optional)
           14. Reload firewalld
           15. Display completion summary


        05.Quay-Verify-deploy.yaml

        tasks:
            1. Check if mirror registry container already running
            2. Skip installation if Quay is already running
            3. Proceed with installation if Quay is not running
            4. Unregister system if already registered
            5. Clean subscription data
            6. Register system to Red Hat
            7. Attach available subscription (auto-attach)
            8. Enable required repositories
            9. Ensure required packages are installed
           10. Create registry directories
           11. Check if mirror registry tarball exists
           12. Fail if mirror registry tarball not found
           13. Extract Mirror Registry package
           14. Run Mirror Registry install script
           15. Copy root-CA certificate
           16. Update CA trust
           17. Verify mirror registry containers
           18. Display Mirror Registry status

            
        06.Quay_Registries.yaml

        tasks:
            1. Ensure .docker directory exists
            2. Deploy combined Docker authentication file
            3. Verify Docker authentication file
            4. Debug output of Docker config


        07.OperatorImages_Mirror.yaml

        tasks:
            1. Ensure oc-mirror binary exists
            2. Create log directory
            3. Create operator directory
            4. Create Mirror  directory
            5. Ensure ISC configuration file exists
            6. Mirror OpenShift images to local disk
            7. Debug oc-mirror disk output
            8. Check if disk mirror output exists
            9. Fail if disk mirror output not created
           10. Mirror from disk to Quay registry 
           11. Debug oc-mirror registry output
           12. Verify mirrored images exist in registry
           13. Debug registry validation

