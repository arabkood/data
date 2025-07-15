1. We have a `pre-commit` hook that do neccessary things before syncing our data to server, it creates auto fields in topics + create bundles to sync to S3, and add them to the commit.

2. We have a `post-receive.prod-only` hook, that we only activate in servers that have access to DB & S3 and that syncs content with db & s3


