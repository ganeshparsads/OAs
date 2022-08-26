package codes;

public class PMatch {
	public static boolean check(int[] a, int[] b)
	{
	    int i = 0;
	    for(i=0;i<26;i++)
	    {
	        if(a[i] != b[i])
	        return false;
	    }
	    return true;
	}

	public static void main(String[] args){
	    String a = "abcbcdcadbb";
	    String b = "abbc";

	    int n = a.length();
	    int m = b.length();
	    int p = 3;
	    int ans = 0;
	    int i, j;

	    int[] arr = new int[26];
	    for(i = 0; i < m; i++)
	        arr[b.charAt(i) - 'a']++;

	    int[][] v = new int[n][26]; 
	    for(i=0;i<p;i++)
	    {   
	        int len = 0;
	        j = i;
	        while(j < n && len != m)
	        {
	            v[i][a.charAt(j) - 'a']++;
	            j += p;
	            len++;
	        }
	        if(len == m && check(arr, v[i]))
	        {
	            ans++;
	        }
	    }
	    for(i = p; i < n; i++)
	    {
	        if(i + ((m - 1) * p) >= n)
	            break;
	        v[i] = v[i-p];
	        v[i][a.charAt(i-p) - 'a']--;
	        v[i][a.charAt(i + ((m- 1) * p)) - 'a']++;
	        if(check(arr, v[i]))
	            ans++;
	    }
	    System.out.println(ans);
	    //return 0;
	}
	
}