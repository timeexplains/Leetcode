import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;
import java.lang.management.ThreadMXBean;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Solution {
	 public double findMedianSortedArrays(int[] nums1, int[] nums2) {
	        int max1 = nums1[nums1.length];
	        int min2 = nums2[0];
	        
	        int index2  = index(max1,nums2);
	        int index1 = index(min2,nums1);
	        
	        int a = (nums1.length-index1);
	        int b = index2;
	        
	        return 0;
	    }
	 
	 public int index(int key,int[] num){
		 return 0;
	 }
	 
	 public static void javacmd(String args[]) {
	        try {
	            Runtime rt = Runtime.getRuntime();
	            Process proc = rt.exec("java");
	            InputStream stderr = proc.getErrorStream();
	            InputStreamReader isr = new InputStreamReader(stderr);
	            BufferedReader br = new BufferedReader(isr);
	            String line = null;
	            System.out.println("<error></error>");
	            while ((line = br.readLine()) != null)
	                System.out.println(line);
	            System.out.println("");
	            int exitVal = proc.waitFor();
	            System.out.println("Process exitValue: " + exitVal);
	        } catch (Throwable t) {
	            t.printStackTrace();
	        }
	    }
	 private static void test() {
		// TODO Auto-generated method stub
//		String procCmd = "wmic process get Caption,CommandLine,KernelModeTime,ReadOperationCount,ThreadCount,UserModeTime,WriteOperationCount";
		 // 取进程信息
//        long[] c0 = readCpu(Runtime.getRuntime().exec(procCmd));
	}
	 
	 public static void main(String[] args)  
	 {
//		 javacmd(args);
		 ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
		 
		 List<String> array = new ArrayList<String>(1000000);
		 for(int i=0;i<1000000;i++){
			 array.add(UUID.randomUUID().toString());
		}
		 try{
			 new Thread(new Runnable() {
				
				@Override
				public void run() {
					 Runtime runtime = Runtime.getRuntime();
					 try {
						Process proc = Runtime.getRuntime().exec("java HelloWorld", null,new File("E:\\javaproject\\Leetcode\\bin"));
						 MemoryMXBean bean = ManagementFactory.getMemoryMXBean();
						 MemoryUsage memoryUsage = bean.getHeapMemoryUsage();
						 System.out.println("judge memory:*"+memoryUsage.getUsed());
						  System.out.println("CPU TIME*"+threadMXBean.getCurrentThreadCpuTime());
						 InputStreamReader isr=new InputStreamReader(proc.getInputStream());    
						 
				            //用缓冲器读行    
				             BufferedReader br=new BufferedReader(isr);    
				             String line=null;    
				            //直到读完为止    
				            while((line=br.readLine())!=null)    
				             {    
				                 System.out.println("inner thread:"+line);    
				             }    
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}).start();;
			 Runtime runtime = Runtime.getRuntime();
			 Process proc = runtime.exec("java HelloWorld", null,new File("E:\\javaproject\\Leetcode\\bin"));
//			 Process proc = Runtime.getRuntime().exec("java -version",null,new File("E:\\javaproject\\Leetcode\\bin"));
//			 Process proc = runtime.exec("javac");
			 //			 Process proc = Runtime.getRuntime().exec("E:\\javaproject\\Leetcode\\bin\\a.bat");
			 //用一个读输出流类去读    
             InputStreamReader isr=new InputStreamReader(proc.getInputStream());    
            //用缓冲器读行    
             BufferedReader br=new BufferedReader(isr);    
             String line=null;    
            //直到读完为止    
            while((line=br.readLine())!=null)    
             {    
                 System.out.println(line);    
             }    
            Map<String,String> map = new HashMap<String,String>(1000000);
   		 	for(int i=0;i<1000000;i++){
   		 		map.put(UUID.randomUUID().toString(),UUID.randomUUID().toString());
   		 	}
   		 MemoryMXBean bean = ManagementFactory.getMemoryMXBean();
		  MemoryUsage memoryUsage = bean.getHeapMemoryUsage();
        System.out.println("Memory:*"+memoryUsage.getUsed());
     

            System.out.println("CPU TIME*"+threadMXBean.getCurrentThreadCpuTime());
		 }catch(Exception e){
			 e.printStackTrace();
		 }
//		proc.getOutputStream();
	}
}
