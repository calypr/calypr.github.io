
## 4.6: Publishing changes to Gen3

In order to publish metadata to CALYPR, regardless of whether you have provided your own metadata or you are simply uploading files to the system, if you want these files to be viewable in the CALYPR site, you will need to publish your data. Publishing data is done with the Forge command line utility.

Since forge relies on your Github repository in order to know which files should have metadata records on the CALYPR platform, a Github personal access token is needed for [source.ohsu.edu](http://source.ohsu.edu) . To create your own personal access token login to [https://source.ohsu.edu/settings/tokens](https://source.ohsu.edu/settings/tokens)  click “generate new token”. Make sure the token has clone permissions at the minimum.

Then run the forge publish command:

\`\`\`forge publish \[your\_generated\_access\_token\]\`\`\`

\[Insert Basic information on explorer page and what it is used for here\]

forge publish \<your-github-token\>

What happens:

1. Forge validates your GitHub Personal Access Token  
2. Packages repository information  
3. Submits a Sower job to Gen3  
4. Gen3 ingests FHIR metadata from META/  
5. Metadata becomes searchable in CALYPR

Successful output:

✓ Personal Access Token validated  
✓ Repository information packaged  
✓ Sower job submitted: job-id-12345  
✓ Metadata ingestion started

Check job status: forge status \<job-id\>  
Get all job ids: forge list

📖 More details: [Forge Publish Command](https://github.com/copilot/tools/forge/commands.md#forge-publish)

---

### Verification Checklist

After completing the workflow:

*  LFS pointer files in Git repository  
*  DRS records created (check .drs/ logs)  
*  DRS URIs point to S3 locations  
*  Metadata files validated successfully  
*  Sower job completed without errors  
*  Data searchable in CALYPR web interface  
*  Can query patients/observations in Gen3  
*  Files accessible via S3 (no duplicate storage)