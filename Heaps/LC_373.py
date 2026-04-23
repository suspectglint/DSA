class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]
        i=0
        j=0
        si=0
        sj=0
        while True:
            #print("Before = ",heap,i,j,si,sj)
            while i<len(nums1) and j<len(nums2):
                if len(heap)==k:
                    #print("Status =",nums1[i]+nums2[j],-heap[0][0])
                    if (nums1[i]+nums2[j])>=-heap[0][0]:
                        #print("Red alert")
                        break
                    else:
                        heapq.heappushpop(heap,(-(nums1[i]+nums2[j]),(nums1[i],nums2[j])))
                else:
                    heap.append((-(nums1[i]+nums2[j]),(nums1[i],nums2[j])))
                    if len(heap)==k:
                        heapq.heapify(heap)
                        #break
                if nums1[i]<nums2[j]:
                    j+=1
                else:
                    i+=1
            if (i==si and j==sj) or (i==len(nums1)-1 and j==len(nums2)-1):
                #print("Heyyah")
                break
            elif i==si:
                i+=1
                si=i
                j=sj
            elif j==sj:
                j+=1
                sj=j
                i=si
            #print("After = ",heap,i,j,si,sj)
        return [a[1] for a in heap] 