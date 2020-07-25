
# kas-devel > GitRepo fetch_cmd shouldn't default to "git fetch --all" [github issue #18]

- [xiUoNPQ0IaU](https://groups.google.com/forum/#!topic/kas-devel/xiUoNPQ0IaU)

## Github issue 18

### 0 NGenetzky commented on issue/18

- [NGenetzky](https://github.com/NGenetzky)
- [issue/18](https://github.com/siemens/kas/issues/18)

The fetch() method for git will call git fetch --all ; this causes issues
because I have 12+ forks added as remotes for one of my layers. It seems like
this should be able to only fetch 'origin', which has been created by kas.

```python
class GitRepo(RepoImpl):
    """
        Provides the git functionality for a Repo.
    """
...
    def fetch_cmd(self):
        return ['git', 'fetch', '--all']
```

### 3 NGenetzky commented on issue/18

- [NGenetzky](https://github.com/NGenetzky)
- [issue/18](https://github.com/siemens/kas/issues/18)

> Would you like to send this as patch with reasoning to kas-devel?

I can, but it won't be immediate. I am still kind of new to the old school patch emailing collaboration approach.

- [x] Create patch
- [x] Submit patch to kas-devel
- [ ] Create PR
- [ ] Await feedback

## Mailing list (xiUoNPQ0IaU)

- [xiUoNPQ0IaU](https://groups.google.com/forum/#!topic/kas-devel/xiUoNPQ0IaU)

### 3 NGenetzky commented on xiUoNPQ0IaU

Submitting patch for review.

- [local](xiUoNPQ0IaU/0001-repos-GitRepo-fetch_cmd-shouldn-t-default-to-git-fet.patch)
- [docs.google.com](https://docs.google.com/viewer?a=v&pid=forums&srcid=MTUxMDY3MjI4MDU2MzY4NzAwODIBMTAxMjM0ODMyMzE3NDA3OTI2NTkBYWtHdHhQcHpDQUFKATAuMQEBdjI&authuser=0)
