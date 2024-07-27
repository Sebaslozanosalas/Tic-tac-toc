from shapes import Grid

class GridManager:
    def __init__(self):
        self.grid = None


    def create_grid(self, screen, color):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Game grid
        grid_margin_ratio = 0.05
        grid_margin = int(screen_width * grid_margin_ratio)
        grid_size = screen_width - (grid_margin * 2)
        grid_line_width = grid_margin // 2
        x_pos = grid_margin
        y_pos = int(screen_height - grid_margin - grid_size)

        self.grid = Grid(
            x_pos = x_pos,
            y_pos = y_pos,
            size = grid_size,
            margin = grid_margin,
            line_width = grid_line_width,
            color = color
        )
    

    def get_cell_coordinates(self):
        # Calculate X positions
        x_start = self.grid.x_pos + (self.grid.cell_size // 2)
        x_positions = [
            x_start + (self.grid.cell_size * i) for i in range(3)
        ]
        
        # Calculate Y positions
        y_start = self.grid.y_pos + (self.grid.cell_size // 2)
        y_positions = [
            y_start + (self.grid.cell_size * i)  for i in range(3)
        ]

        # Make final positions
        cell_coordinates = []
        for y_pos in y_positions:
            cell_coordinates.append(
                [(x_pos, y_pos) for x_pos in x_positions]
            )

        return cell_coordinates
    

    def get_cell_limits(self):
        x_limits = [
            self.grid.x_pos + (self.grid.cell_size * i) for i in range(1, 4)
        ]
        y_limits = [
            self.grid.y_pos + (self.grid.cell_size * i) for i in range(1, 4)
        ]
        return(x_limits, y_limits)
    

    def get_cell_clicked(self, click_pos):
        x_click_pos, y_click_pos = click_pos

        x_limits, y_limits = self.get_cell_limits()
        for i in range(3):
            if x_click_pos < x_limits[i]:
                x_cell_idx = i 
                break
        for i in range(3):
            if y_click_pos < y_limits[i]:
                y_cell_idx = i 
                break
        
        return (x_cell_idx, y_cell_idx)
        

    def clicked_in_cell(self, click_pos):
        x_click_pos, y_click_pos = click_pos

        # Validate x position inside grid
        if x_click_pos > self.grid.x_pos \
            and x_click_pos < (self.grid.x_pos + self.grid.size):
            # Validate y position inside grid
            if y_click_pos > self.grid.y_pos \
                and y_click_pos < (self.grid.y_pos + self.grid.size):
                return True
        
        return False
    
