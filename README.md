openshift/01.download_install_prepare_ocp4_binaries.yaml        
tasks: 

	  1. Create temporary ocp binaries directory - /tmp/openshift-tools TAGS: []
	  2. Create temporary mirror-registry directory /tmp/mirror-registry        TAGS: []
	  3. Download oc-mirror binaries    TAGS: []
	  4. Download OpenShift Client (oc & kubectl) binary        TAGS: []
	  5. Download OpenShift Installer binary    TAGS: []
	  6. Download Mirror Registry       TAGS: []
	  7. Extract all ocp binaries tarballs      TAGS: []
  	  8. Ensure binaries are executable TAGS: []
	  9. Clean up temporary directories but not mirror-registry directory       TAGS: []
	  10. Verify installation - oc version      TAGS: []
	  11. Display oc version    TAGS: []

openshift/02.prepare_install_config_manifests.yaml
tasks:

      1. Ensure required packages are installed (Apache + dependencies) TAGS: []
      2. Ensure Apache service is enabled and running   TAGS: []
      3. Ensure OpenShift installation directory exists TAGS: []
      4. Create install-config.yaml for OpenShift 4     TAGS: []
      5. Verify install-config.yaml exists      TAGS: []
      6. Fail if install-config.yaml is missing TAGS: []
      7. Generate OpenShift manifests   TAGS: []
      8. Generate ignition configs      TAGS: []
      9. Ensure web server directory exists     TAGS: []
      10. Find ignition files in OpenShift installation directory       TAGS: []
      11. Copy ignition files to web server directory   TAGS: []
      12. Adjust permissions for ignition files TAGS: []
      13. Restarting Apache service     TAGS: []
      14. Disable Firewalld Service     TAGS: []
      15. Display completion summary    TAGS: []


openshift/03.quay_mirror_registry_configure.yaml
tasks: 

      1. Unregister system if already registered (optional cleanup)     TAGS: []
      2. Clean subscription data        TAGS: []
      3. Register system to Red Hat     TAGS: []
      4. Attach available subscription (auto-attach)    TAGS: []
      5. Enable required repositories   TAGS: []
      6. Ensure required packages are installed TAGS: []
      7. Create registry directories    TAGS: []
      8. Extract Mirror Registry package        TAGS: []
      9. Run Mirror Registry install script     TAGS: []
      10. Ensure Mirror Registry service is running     TAGS: []
      11. Copy root-CA certificate      TAGS: [one]
      12. Update CA trust       TAGS: [two]
      13. Display Mirror Registry status        TAGS: [three]


openshift/04.mirror_registry_integrity_validation.yaml
tasks:

      Check if mirror registry container already running        TAGS: []
      Skip installation if Quay is already running      TAGS: []
      Unregister system if already registered   TAGS: []
      Clean subscription data   TAGS: []
      Register system to Red Hat        TAGS: []
      Attach available subscription (auto-attach)       TAGS: []
      Enable required repositories      TAGS: []
      Ensure required packages are installed    TAGS: []
      Create registry directories       TAGS: []
      Check if mirror registry tarball exists   TAGS: []
      Fail if mirror registry tarball not found TAGS: []
      Extract Mirror Registry package   TAGS: []
      Run Mirror Registry install script        TAGS: []
      Copy root-CA certificate  TAGS: []
      Update CA trust   TAGS: []
      Verify mirror registry containers TAGS: []
      Display Mirror Registry status    TAGS: []


            
openshift/05.quay_docker_config_registries.yaml
tasks:

      Ensure .docker directory exists   TAGS: []
      Deploy combined Docker authentication file        TAGS: []
      Verify Docker authentication file TAGS: []
      Debug output of Docker config     TAGS: []

openshift/06.precheck_environment_before_deploy.yaml
tasks:

      Display system summary    TAGS: []
      Check minimum CPU cores   TAGS: []
      Check minimum memory      TAGS: []
      Check SELinux status      TAGS: []
      Display SELinux status    TAGS: []
      Verify required OpenShift binaries are present    TAGS: []
      Fail if any required binary is missing    TAGS: []
      Display binary paths      TAGS: []
      Ensure Docker authentication config exists        TAGS: []
      Fail if Docker authentication config is missing   TAGS: []
      Validate registry authentication JSON format      TAGS: []
      Validate access to Red Hat registries     TAGS: []
      Show registry access results      TAGS: []
      Check access to internal Quay mirror      TAGS: []
      Display Quay mirror health        TAGS: []
      Verify DNS resolution for registries      TAGS: []
      Verify presence of required deployment playbooks  TAGS: []
      Display verified playbook list    TAGS: []
      Display final precheck summary    TAGS: []

openshift/07.mirroring_operator_images.yaml
tasks:

      Ensure oc-mirror binary exists    TAGS: []
      Create log directory      TAGS: []
      Create operator directory TAGS: []
      Create Mirror  directory  TAGS: []
      ansible.builtin.copy      TAGS: []
      Ensure ISC configuration file exists      TAGS: []
      Mirror OpenShift images to local disk     TAGS: []
      Debug oc-mirror disk output       TAGS: []
      Check if disk mirror output exists        TAGS: []
      Create mirror output directory if missing TAGS: []
      Fail if disk mirror output not created    TAGS: []
      Mirror from disk to Quay registry TAGS: [push]
      Debug oc-mirror registry output   TAGS: [show]
      Verify mirrored images exist in registry  TAGS: [verify]
      Debug registry validation TAGS: [output]

openshift/08.mirroring_retry_push_operators.yaml
tasks:

      Ensure oc-mirror binary exists    TAGS: []
      Ensure required directories exist TAGS: []
      Write ImageSetConfiguration file  TAGS: []
      Mirror OpenShift images to local disk     TAGS: []
      Fail if disk mirror output not created    TAGS: []
      Stop play if disk mirror output missing   TAGS: []
      Mirror from disk to Quay registry (initial attempt)       TAGS: [push]
      Check for push errors in oc-mirror logs   TAGS: [check]
      Retry mirroring failed operator images    TAGS: [retry]
      Report final status       TAGS: []
      Verify Quay registry health       TAGS: []
      Show summary and log pointers     TAGS: []
