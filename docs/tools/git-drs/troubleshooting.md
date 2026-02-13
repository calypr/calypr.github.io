# Git DRS — Troubleshooting

Common issues and solutions when working with Git DRS.

## When to Use Which Tool

Understanding when to use Git, Git LFS, or Git DRS commands:

| Tool | Commands | When to Use |
|------|----------|-------------|
| **Git DRS** | `git drs init`<br>`git drs remote add`<br>`git drs remote list`<br>`git drs fetch`<br>`git drs push` | Repository and remote configuration<br>Setting up a new repository<br>Adding/managing DRS remotes<br>Refreshing expired credentials<br>Cross-remote promotion |
| **Git LFS** | `git lfs track`<br>`git lfs ls-files`<br>`git lfs pull`<br>`git lfs untrack` | File tracking and management<br>Defining which files to track<br>Downloading specific files<br>Checking file localization status |
| **Standard Git** | `git add`<br>`git commit`<br>`git push`<br>`git pull` | Version control operations<br>Normal development workflow<br>Git DRS runs automatically in background |

## Authentication Errors

### Error: `Upload error: 403 Forbidden` or `401 Unauthorized`

**Cause**: Expired or invalid credentials

**Solution**:

```bash
# Download new credentials from your data commons
# Then refresh them by re-adding the remote
git drs remote add gen3 production \
    --cred /path/to/new-credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket
```

**Prevention**:

- Credentials expire after 30 days
- Set a reminder to refresh them regularly

### Error: `Upload error: 503 Service Unavailable`

**Cause**: DRS server is temporarily unavailable or credentials expired

**Solutions**:

1. Wait and retry the operation
2. Refresh credentials:
   ```bash
   git drs remote add gen3 production \
       --cred /path/to/credentials.json \
       --url https://calypr-public.ohsu.edu \
       --project my-project \
       --bucket my-bucket
   ```
3. If persistent, download new credentials from the data commons

## Network Errors

### Error: `net/http: TLS handshake timeout`

**Cause**: Network connectivity issues

**Solution**:

- Simply retry the command
- These are usually temporary network issues

### Error: Git push timeout during large file uploads

**Cause**: Long-running operations timing out

**Solution**: Add to `~/.ssh/config`:

```
Host github.com
    TCPKeepAlive yes
    ServerAliveInterval 30
```

## File Tracking Issues

### Files Not Being Tracked by LFS

**Symptoms**:

- Large files committed directly to Git
- `git lfs ls-files` doesn't show your files

**Solution**:

```bash
# Check what's currently tracked
git lfs track

# Track your file type
git lfs track "*.bam"
git add .gitattributes

# Remove from Git and re-add
git rm --cached large-file.bam
git add large-file.bam
git commit -m "Track large file with LFS"
```

### Error: `[404] Object does not exist on the server`

**Symptoms**:

- After clone, git pull fails

**Solution**:

```bash
# Confirm repo has complete configuration
git drs remote list

# Initialize your git drs project
git drs init

# Add remote configuration
git drs remote add gen3 production \
    --cred /path/to/credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket

# Attempt git pull again
git lfs pull -I path/to/file
```

### Files Won't Download

**Cause**: Files may not have been properly uploaded or DRS records missing

**Solution**:

```bash
# Check repository status
git drs remote list

# Try pulling with verbose output
git lfs pull -I "problematic-file*" --verbose

# Check logs
cat .git/drs/*.log
```

## Configuration Issues

### Empty or Incomplete Configuration

**Error**: `git drs remote list` shows empty or incomplete configuration

**Cause**: Repository not properly initialized or no remotes configured

**Solution**:

```bash
# Initialize repository if needed
git drs init

# Add Gen3 remote
git drs remote add gen3 production \
    --cred /path/to/credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket

# Verify configuration
git drs remote list
```

### Configuration Exists but Commands Fail

**Cause**: Mismatched configuration between global and local settings, or expired credentials

**Solution**:

```bash
# Check configuration
git drs remote list

# Refresh credentials by re-adding the remote
git drs remote add gen3 production \
    --cred /path/to/new-credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket
```

## Remote Configuration Issues

### Error: `no default remote configured`

**Cause**: Repository initialized but no remotes added yet

**Solution**:

```bash
# Add your first remote (automatically becomes default)
git drs remote add gen3 production \
    --cred /path/to/credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket
```

### Error: `default remote 'X' not found`

**Cause**: Default remote was deleted or configuration is corrupted

**Solution**:

```bash
# List available remotes
git drs remote list

# Set a different remote as default
git drs remote set staging

# Or add a new remote
git drs remote add gen3 production \
    --cred /path/to/credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project my-project \
    --bucket my-bucket
```

### Commands Using Wrong Remote

**Cause**: Default remote is not the one you want to use

**Solution**:

```bash
# Check current default
git drs remote list

# Option 1: Change default remote
git drs remote set production

# Option 2: Specify remote for single command
git drs push staging
git drs fetch production
```

## Undoing Changes

### Untrack LFS Files

If you accidentally tracked the wrong files:

```bash
# See current tracking
git lfs track

# Remove incorrect pattern
git lfs untrack "wrong-dir/**"

# Add correct pattern
git lfs track "correct-dir/**"

# Stage the changes
git add .gitattributes
git commit -m "Fix LFS tracking patterns"
```

### Undo Git Add

Remove files from staging area:

```bash
# Check what's staged
git status

# Unstage specific files
git restore --staged file1.bam file2.bam

# Unstage all files
git restore --staged .
```

### Undo Last Commit

To retry a commit with different files:

```bash
# Undo last commit, keep files in working directory
git reset --soft HEAD~1

# Or undo and unstage files
git reset HEAD~1

# Or completely undo commit and changes (BE CAREFUL!)
git reset --hard HEAD~1
```

### Remove Files from LFS History

If you committed large files directly to Git by mistake:

```bash
# Remove from Git history (use carefully!)
git filter-branch --tree-filter 'rm -f large-file.dat' HEAD

# Then track properly with LFS
git lfs track "*.dat"
git add .gitattributes
git add large-file.dat
git commit -m "Track large file with LFS"
```

## Diagnostic Commands

### Check System Status

```bash
# Git DRS version and help
git-drs version
git-drs --help

# Configuration
git drs remote list

# Repository status
git status
git lfs ls-files
```

### Test Connectivity

```bash
# Test basic Git operations
git lfs pull --dry-run

# Test DRS configuration
git drs remote list
```

### Log Analysis

When reporting issues, include:

```bash
# System information
git-drs version
git lfs version
git --version

# Configuration
git drs remote list
```

## Prevention Best Practices

1. **Refresh credentials regularly** -- Credentials expire after 30 days. Set a calendar reminder to download and configure new credentials before they expire.

2. **Test in small batches** -- Don't commit hundreds of files at once. Start with a few files to ensure your configuration works correctly.

3. **Verify tracking** -- Always check `git lfs ls-files` after adding files to ensure they're being tracked by LFS.

4. **Use .gitignore** -- Prevent accidental commits of temporary files, build artifacts, and other files that shouldn't be in the repository.

5. **Monitor repository size** -- Keep an eye on `.git` directory size. If it grows unexpectedly, you may have committed large files directly to Git instead of through LFS.

## Getting Help

For issues not covered in this guide:

- Check the [Git DRS Quick Start](quickstart.md) for setup instructions
- Review the [Developer Guide](developer-guide.md) for advanced usage
- Consult the [Git LFS FAQ](https://github.com/git-lfs/git-lfs/wiki/FAQ)
- See [GitHub's Git LFS documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
