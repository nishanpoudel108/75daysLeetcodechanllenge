use std::collections::BTreeSet;

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mx = 50000;
        let mut seg = vec![0; (mx as usize) << 2];
        
        fn update(seg: &mut Vec<i32>, idx: i32, val: i32, p: usize, l: i32, r: i32) {
            if l == r {
                seg[p] = val;
                return;
            }
            let mid = (l + r) >> 1;
            if idx <= mid {
                update(seg, idx, val, p << 1, l, mid);
            } else {
                update(seg, idx, val, p << 1 | 1, mid + 1, r);
            }
            seg[p] = seg[p << 1].max(seg[p << 1 | 1]);
        }
        
        fn query(seg: &Vec<i32>, L: i32, R: i32, p: usize, l: i32, r: i32) -> i32 {
            if L <= l && r <= R {
                return seg[p];
            }
            let mid = (l + r) >> 1;
            let mut res = 0;
            if L <= mid {
                res = res.max(query(seg, L, R, p << 1, l, mid));
            }
            if R > mid {
                res = res.max(query(seg, L, R, p << 1 | 1, mid + 1, r));
            }
            res
        }
        
        let mut st = BTreeSet::new();
        st.insert(0);
        st.insert(mx);
        update(&mut seg, mx, mx, 1, 0, mx);
        let mut ans = Vec::new();
        
        for q in queries {
            if q[0] == 1 {
                let x = q[1];
                let r = st.range((x + 1)..).next().copied().unwrap_or(mx);
                let l = st.range(..x).next_back().copied().unwrap_or(0);
                update(&mut seg, x, x - l, 1, 0, mx);
                update(&mut seg, r, r - x, 1, 0, mx);
                st.insert(x);
            } else {
                let x = q[1];
                let sz = q[2];
                let pre = st.range(..=x).next_back().copied().unwrap_or(0);
                let max_space = query(&seg, 0, pre, 1, 0, mx).max(x - pre);
                ans.push(max_space >= sz);
            }
        }
        
        ans
    }
}