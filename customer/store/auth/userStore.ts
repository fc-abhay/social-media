import axiosClient from "@/utils/axiosClient";
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";


interface user{
    email:string,
    username:string,
    posts:any[],
    id:string
}
interface UserState {
    user: user | null;
    loading: boolean;
    error: string | null;
}

export const fetchUserInfo = createAsyncThunk(
    "user/fetchUserInfo",
    async (_, { rejectWithValue }) => {
        try {
            const { data } = await axiosClient.get("/auth/get-user-info/");
            return data;
        } catch (error:any) {
            return rejectWithValue(error?.response?.data || "Error fetching user info");
        }
    }
);


const initialState: UserState = {
    user:null,
    loading: false,
    error: null,
};

const userInfo=createSlice({
    name:"userInfo",
    initialState,
    reducers:{
        logout:(state)=>{
            state.user=null;
            localStorage.removeItem("token")
        }
    },
    extraReducers(builder) {
        builder
        .addCase(fetchUserInfo.pending, (state)=>{
            state.loading=true;
            state.error=null
        })
        .addCase(fetchUserInfo.fulfilled, (state,action)=>{
            state.loading=false;
            state.user=action.payload.user
        })
        .addCase(fetchUserInfo.rejected, (state,action)=>{
            state.loading=false;
            state.error = (action.payload as string) || "Failed to load";
        })
    },
})

export const {logout} = userInfo.actions;

export default userInfo.reducer