# Development and Deployment Reflection

## Key Challenges Faced

### 1. Docker Hub Authentication Error
**Problem:** Pipeline failed during Docker push due to a naming mismatch in GitHub secrets.
- Used `DOCKER_USERNAME` instead of `DOCKERHUB_USERNAME` in workflow file
- Spent extensive time debugging what seemed like a token issue

**Solution:** 
- Hardcoded username in workflow to test if token was valid (it was)
- Discovered the naming discrepancy by comparing workflow file to GitHub secrets
- Fixed by using correct secret name: `DOCKERHUB_USERNAME`

### 2. Git File Tracking Issue
**Problem:** Files appeared as 0 bytes in commits despite having content locally.
- Tests failed in GitHub Actions with missing file errors
- Commit history showed files being pushed with 0 bytes

**Solution:**
- Files weren't properly staged before committing
- Fixed by ensuring proper `git add` and checking with `git status` before pushing
- Added verification steps in workflow to catch missing files early

### 3. Local Testing Limitations
**Problem:** Unable to run Playwright tests locally due to sudo permission requirements.

**Solution:**
- Used GitHub Actions as primary testing environment
- Split tests into unit tests (local) and integration tests (CI/CD only)
- This slowed development but ensured consistent test environment

