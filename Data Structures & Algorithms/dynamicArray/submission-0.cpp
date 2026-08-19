class DynamicArray {
    int *nums;
    int global_capacity;
    int index = 0;
public:

    DynamicArray(int capacity) : global_capacity(capacity), index(0) {
        nums = new int[capacity];
    }

    int get(int i) {
        return nums[i];
    }

    void set(int i, int n) {
        nums[i] = n;
    }

    void pushback(int n) {
        if (index == global_capacity) {
            resize();
        }
        nums[index] = n;
        index += 1;
    }

    int popback() {
        index -= 1;
        int popped = nums[index];
        nums[index] = 0;
        return popped;
    }

    void resize() {
        int *new_array = new int[global_capacity*2];
        for (int i = 0; i < global_capacity; i++) {
            new_array[i] = nums[i];
        }
        delete[] nums;
        nums = new_array;
        global_capacity *= 2;
    }

    int getSize() {
        return index;
    }

    int getCapacity() {
        return global_capacity;
    }
};
