# Git 問題排除紀錄

## 問題一：.DS_Store 被 Git 追蹤

### 發生原因
`.DS_Store` 是 macOS 自動產生的隱藏檔案，儲存 Finder 的排列資訊，與程式碼無關，但被 Git 誤追蹤。

### 解決方式

1. 建立 `.gitignore` 檔案，加入以下內容：
    ```
    # macOS
    .DS_Store
    ```

2. 把已經被追蹤的 `.DS_Store` 從 Git 快取中移除：
    ```
    git restore --staged .DS_Store week13/.DS_Store
    git rm -r --cached .DS_Store week13/.DS_Store
    ```

3. Commit 變更：
    ```
    git add .gitignore
    git commit -m "Add .gitignore and remove .DS_Store from tracking"
    ```

---

## 問題二：push 被拒絕（diverged）

### 發生原因
本地和遠端的 commit 歷史分叉（diverged），遠端有本地沒有的 commit，導致 push 失敗。

### 錯誤訊息
```
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

### 解決方式
先執行 `git pull --rebase`，把遠端變更套用在本地 commit 前面，再 push：
```
git pull --rebase
git push
```

---

## 問題三：rebase 過程中 .DS_Store 造成衝突

### 發生原因
在執行 `git pull --rebase` 的過程中，`.DS_Store` 檔案衝突導致 rebase 卡住，進入 detached HEAD 狀態。

### 錯誤訊息
```
error: The following untracked working tree files would be overwritten by merge:
    .DS_Store
    week13/.DS_Store
Please move or remove them before you merge.
```

### 解決方式

1. 刪除造成衝突的 `.DS_Store` 檔案：
    ```
    rm -f .DS_Store week13/.DS_Store
    ```

2. 繼續完成 rebase：
    ```
    git rebase --continue
    ```

3. 成功後再 push：
    ```
    git push
    ```

---

## 日常上傳流程（正常情況）

```
git add .
git commit -m "說明你做了什麼"
git push
```

> 如果有多台電腦或多人協作，push 前建議先 `git pull`。
