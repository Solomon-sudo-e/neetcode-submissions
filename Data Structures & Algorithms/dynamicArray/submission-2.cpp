class DynamicArray {
    int *nums;
    int index;
    int arr_capacity;
public:

    DynamicArray(int capacity): index(0), arr_capacity(capacity) {
        nums = new int[capacity];
    }

    int get(int i) {
        return nums[i];
    }

    void set(int i, int n) {
        nums[i] = n;
    }

    void pushback(int n) {
        if(index == arr_capacity) {
            resize();
        }

        nums[index] = n;
        index+=1;
    }

    int popback() {
        index -= 1;
        int popped = nums[index];
        nums[index] = 0;
        return popped;
    }

    void resize() {
        int *new_arr = new int[arr_capacity*2];
        for(int i = 0; i < index; i++) {
            new_arr[i] = nums[i];
        }
        arr_capacity *= 2;
        nums = new_arr;
    }

    int getSize() {
        return index;
    }

    int getCapacity() {
        return arr_capacity;
    }
};
