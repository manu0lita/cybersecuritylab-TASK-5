# Final Submission Checklist

## A. Finish the actual lab (required before calling this complete)
- [ ] Verify DVWA responds at the exact local URL used in the report.
- [ ] Capture a fresh environment screenshot.
- [ ] Capture baseline input `1`.
- [ ] Capture the quote-test result.
- [ ] Capture the true-condition and false-condition comparison.
- [ ] Record whether SQLi was confirmed, not confirmed, or inconclusive.
- [ ] Export or inspect the actual web logs around the test time where available.
- [ ] If only using `scripts/sample_access.log`, label it synthetic in the report and video.
- [ ] Complete incident response notes with actual detection/containment steps.
- [ ] Do not claim remediation was completed unless a fix was applied and retested.

## B. Finish the report
- [ ] Replace every `[FILL IN]`, `[VERIFY]`, or bracketed result placeholder.
- [ ] Add the actual E01-E06 screenshots.
- [ ] Update finding severity and rationale based on actual evidence.
- [ ] Keep the limitation statement about the offline pattern detector.
- [ ] Re-export and inspect the final PDF.

## C. Publish GitHub repository
From the extracted project folder, after reviewing evidence for secrets:

```bash
git init
git add README.md docs diagrams scripts report evidence FINAL_SUBMISSION_CHECKLIST.md .gitignore
git commit -m "Add DVWA SQL injection capstone project"
```

Create an empty repository on GitHub, then follow GitHub's instructions to set the remote and push. Review files before publishing; do not commit session cookies, tokens, raw unreviewed logs, or unrelated personal data.

Suggested repository name: `dvwa-sqli-incident-response-capstone`

## D. Record the final 12-minute video
- [ ] Replace bracketed prompts in `docs/05_12_minute_video_script.md` with actual results.
- [ ] Show the browser, key commands, evidence register, log detection, and report.
- [ ] Rehearse and time the script.
- [ ] Upload to the approved hosting platform and test the link.

## E. Final links
- Report PDF: `[ADD HOSTED PDF LINK]`
- GitHub repository: `[ADD REPOSITORY LINK]`
- 12-minute video: `[ADD VIDEO LINK]`

**Do not submit this starter kit PDF unchanged.** The final report must reflect the actual results you observed.
