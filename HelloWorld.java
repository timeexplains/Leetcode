import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;
import java.lang.management.ThreadMXBean;
public class HelloWorld {
	public static void main(String[] args) {
		
		ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
	
		for(int i=0;i<10000000;i++);
		System.out.println("Hello.");
		MemoryMXBean memoryMXBean = ManagementFactory.getMemoryMXBean();
		MemoryUsage memoryUsage = memoryMXBean.getHeapMemoryUsage(); //椎内存使用情况
		long totalMemorySize = memoryUsage.getInit(); //初始的总内存
		long maxMemorySize = memoryUsage.getMax(); //最大可用内存
		long usedMemorySize = memoryUsage.getUsed(); //已使用的内存
		System.out.println(usedMemorySize);
		System.out.println(threadMXBean.getCurrentThreadCpuTime());
	}

}
