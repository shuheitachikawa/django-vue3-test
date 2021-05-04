export interface User {
  name: string;
}

export interface Good {
  user_id: string;
}

export interface Tweet {
  id: string;
  content: string;
  created_at: string;
  user: User;
  good: Good[];
}
