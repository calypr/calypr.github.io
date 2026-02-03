## 4.6: Publishing changes to Gen3

In order to publish metadata to CALYPR, regardless of whether you have provided your own metadata or you are simply uploading files to the system, you will need to publish your data. Publishing data is done with the **Forge** command line utility.

Since Forge relies on your GitHub repository to know which files should have metadata records on the CALYPR platform, a GitHub Personal Access Token (PAT) is needed. To create your own PAT, login to [https://source.ohsu.edu](https://source.ohsu.edu), go to Settings > Tokens, and click "Generate new token". Make sure the token has `clone` permissions at the minimum.

To publish, run:
```bash
forge publish [your_PAT]
```

### Publishing Process

To publish your metadata, run the following command:

```bash
forge publish <your-github-token>
```

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
*  DRS records created
*  DRS URIs point to S3 locations  
*  Metadata files validated successfully  
*  Sower job completed without errors  
*  Data searchable in CALYPR web interface  
*  Can query patients/observations in Gen3  
*  Files accessible via S3 (no duplicate storage)